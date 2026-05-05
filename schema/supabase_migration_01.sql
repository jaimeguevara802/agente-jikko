-- ==============================================================================
-- Migración de PM Operating System (Airtable -> Supabase PostgreSQL)
-- ==============================================================================

-- 1. Projects
CREATE TABLE public.projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    name TEXT NOT NULL,
    project_code TEXT UNIQUE NOT NULL,
    status TEXT, -- Discovery, Planned, In Progress, Blocked, Done, Archived
    business_area TEXT,
    owner TEXT,
    team TEXT,
    summary TEXT
);

-- 2. Teams
CREATE TABLE public.teams (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    name TEXT NOT NULL,
    lead TEXT,
    area TEXT,
    notes TEXT
);

-- 3. Meetings
CREATE TABLE public.meetings (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    team_id UUID REFERENCES public.teams(id) ON DELETE SET NULL,
    meeting_type TEXT, -- ASIS, TOBE, Follow-up, Planning, Decision, Risk, Other
    meeting_date TIMESTAMP WITH TIME ZONE,
    participants TEXT,
    source TEXT,
    notes TEXT
);

-- 4. Transcripts
CREATE TABLE public.transcripts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    meeting_id UUID REFERENCES public.meetings(id) ON DELETE CASCADE,
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    team_id UUID REFERENCES public.teams(id) ON DELETE SET NULL,
    raw_transcript TEXT NOT NULL,
    source_url TEXT,
    immutable BOOLEAN DEFAULT true,
    imported_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- 5. Draft Insights
CREATE TABLE public.draft_insights (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    meeting_id UUID REFERENCES public.meetings(id) ON DELETE SET NULL,
    draft_type TEXT, -- Business Context, ASIS, TOBE, Capability...
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    status TEXT, -- Draft, In Review, Approved Candidate, Rejected, Archived
    version_hint INTEGER DEFAULT 1
);

-- 6. Approved Context
CREATE TABLE public.approved_context (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    context_type TEXT, -- Business Context, ASIS, TOBE...
    title TEXT NOT NULL,
    approved_content TEXT NOT NULL,
    version INTEGER DEFAULT 1,
    status TEXT, -- Active, Superseded, Archived
    source_references TEXT,
    approved_by TEXT,
    approved_at TIMESTAMP WITH TIME ZONE
);

-- 7. OKRs
CREATE TABLE public.okrs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    team_id UUID REFERENCES public.teams(id) ON DELETE SET NULL,
    objective TEXT NOT NULL,
    key_result TEXT NOT NULL,
    metric_name TEXT,
    baseline NUMERIC,
    target NUMERIC,
    current_value NUMERIC,
    due_date TIMESTAMP WITH TIME ZONE,
    status TEXT -- On Track, At Risk, Off Track, Done
);

-- 8. Capabilities
CREATE TABLE public.capabilities (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT,
    priority TEXT, -- High, Medium, Low
    status TEXT -- Proposed, Approved, In Progress, Done, Dropped
);

-- 9. Features
CREATE TABLE public.features (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    capability_id UUID REFERENCES public.capabilities(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT,
    priority TEXT,
    status TEXT
);

-- 10. User Stories
CREATE TABLE public.user_stories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    feature_id UUID REFERENCES public.features(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    narrative TEXT,
    acceptance_criteria TEXT,
    status TEXT -- Draft, Approved, Planned, In Progress, Done, Dropped
);

-- 11. Decisions
CREATE TABLE public.decisions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    decision TEXT NOT NULL,
    rationale TEXT,
    decision_date TIMESTAMP WITH TIME ZONE,
    status TEXT -- Active, Superseded, Rejected
);

-- 12. Risks
CREATE TABLE public.risks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    impact TEXT, -- High, Medium, Low
    probability TEXT, -- High, Medium, Low
    mitigation TEXT,
    status TEXT -- Open, Watching, Mitigated, Closed
);

-- 13. Followups
CREATE TABLE public.followups (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    team_id UUID REFERENCES public.teams(id) ON DELETE SET NULL,
    title TEXT NOT NULL,
    commitment TEXT,
    owner TEXT,
    due_date TIMESTAMP WITH TIME ZONE,
    status TEXT -- Open, In Progress, Done, Delayed, Cancelled
);

-- 14. Milestones
CREATE TABLE public.milestones (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    project_id UUID REFERENCES public.projects(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    description TEXT,
    target_date TIMESTAMP WITH TIME ZONE,
    status TEXT -- Upcoming, On Track, At Risk, Missed, Done
);

-- Función para auto-actualizar updated_at en Supabase
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Aplicar trigger a todas las tablas para actualizar el timestamp
CREATE TRIGGER update_projects_modtime BEFORE UPDATE ON public.projects FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_teams_modtime BEFORE UPDATE ON public.teams FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_meetings_modtime BEFORE UPDATE ON public.meetings FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_transcripts_modtime BEFORE UPDATE ON public.transcripts FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_draft_insights_modtime BEFORE UPDATE ON public.draft_insights FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_approved_context_modtime BEFORE UPDATE ON public.approved_context FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_okrs_modtime BEFORE UPDATE ON public.okrs FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_capabilities_modtime BEFORE UPDATE ON public.capabilities FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_features_modtime BEFORE UPDATE ON public.features FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_user_stories_modtime BEFORE UPDATE ON public.user_stories FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_decisions_modtime BEFORE UPDATE ON public.decisions FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_risks_modtime BEFORE UPDATE ON public.risks FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_followups_modtime BEFORE UPDATE ON public.followups FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
CREATE TRIGGER update_milestones_modtime BEFORE UPDATE ON public.milestones FOR EACH ROW EXECUTE PROCEDURE update_updated_at_column();
