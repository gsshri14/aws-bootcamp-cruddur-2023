select 
    activities.uuid,
    users.display_name,
    users.handle,
    activities.message,
    activities.created_at,
    activities.expires_at
from 
    public.activities
inner join 
    public.users on user.uuid = activities.user_uuid
where 
    activities.uuid = %(uuid)s;