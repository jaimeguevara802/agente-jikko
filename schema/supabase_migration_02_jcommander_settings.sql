-- ==============================================================================
-- Migración para J-Commander: Ajustes de Contraseña Global e Invitados
-- ==============================================================================

-- 1. Crear la tabla de ajustes generales (para la contraseña global y otras configuraciones futuras)
CREATE TABLE IF NOT EXISTS public.app_settings (
    key TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 2. Insertar una contraseña global por defecto si no existe ('jcommander2026')
INSERT INTO public.app_settings (key, value)
VALUES ('global_password', 'jcommander2026')
ON CONFLICT (key) DO NOTHING;

-- 3. Habilitar RLS en la tabla para impedir lectura directa desde clientes anónimos
ALTER TABLE public.app_settings ENABLE ROW LEVEL SECURITY;

-- 4. Crear política para que solo los administradores autenticados (Admin de Supabase Auth) puedan leer o escribir ajustes
CREATE POLICY "Allow authenticated users to read/update settings"
ON public.app_settings
FOR ALL
TO authenticated
USING (true)
WITH CHECK (true);

-- 5. Crear la función RPC para verificar la contraseña de forma segura (ejecutable públicamente por anon/invitados)
CREATE OR REPLACE FUNCTION public.verify_global_password(password_attempt TEXT)
RETURNS BOOLEAN AS $$
DECLARE
    stored_password TEXT;
BEGIN
    SELECT value INTO stored_password FROM public.app_settings WHERE key = 'global_password';
    RETURN stored_password = password_attempt;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
