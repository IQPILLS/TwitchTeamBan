from twitchAPI.twitch import Twitch
from twitchAPI.oauth import UserAuthenticator
from twitchAPI.types import AuthScope

twitch = Twitch('app_id', 'app_secret')

username = 'vewaaaa'    # your twitch nickanme
reason = 'Test'    # ban reason
target_scope = [AuthScope.MODERATOR_MANAGE_BANNED_USERS]
auth = UserAuthenticator(twitch, target_scope, force_verify=False)
token, refresh_token = auth.authenticate()
twitch.set_user_authentication(token, target_scope, refresh_token)
uid = twitch.get_users(logins=username)['data'][0]['id']

data = twitch.get_teams(name='spsquad')['data'][0]['users']
b = 0
for _ in range(len(data)):
    ban_id = data[b]['user_id']
    try:
        twitch.ban_user(broadcaster_id=uid, moderator_id=uid, reason=reason, user_id=ban_id)
        print(data[b]['user_name'] + ' banned.')
    except:
        print(data[b]['user_name'] + ' already banned.')
    b += 1
