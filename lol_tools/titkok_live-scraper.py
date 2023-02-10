from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import EnvelopeEvent,EmoteEvent,MicBattleEvent,CommentEvent, ConnectEvent, GiftEvent,ShareEvent,LikeEvent,FollowEvent, ViewerCountUpdateEvent,LiveEndEvent,JoinEvent
from pystyle import Write, Colors,Colorate
import time

color1 = Colors.red_to_yellow
color2 = Colors.green_to_blue
color3 = Colors.blue_to_red
color4 = Colors.red_to_purple
color5 = Colors.purple_to_blue
color6 = Colors.blue_to_cyan
color7 = Colors.cyan_to_green
color8 = Colors.green_to_red
color9 = Colors.red_to_blue
color10 = Colors.blue_to_white
color11 = Colors.green_to_white

id_chu_phong = input('Nhập ID chủ phòng đang live :')
client: TikTokLiveClient = TikTokLiveClient(unique_id=f"@{id_chu_phong}")

@client.on('connect')
async def on_connect(_: ConnectEvent):
    print('connected sucess', client.room_id)
#@client.on("join")
#async def on_join(event: JoinEvent):
#    Write.Print(f"{event.user.uniqueId} vừa tham gia vào phòng live \n",color9,interval=0.00000000000015) 
@client.on('comment')
async def on_comment(event: CommentEvent):
    
    Write.Print(f"[COMMENT] {event.user.uniqueId} : {event.comment} \n",color7,interval=0.00000000000015)
@client.on('gift')
async def on_gift(event: GiftEvent):
    
    if event.gift.gift_type == 1:
        if event.gift.repeat_end == 1:
            print(f"{event.user.uniqueId} gửi cho chủ phòng {event.gift.repeat_count}x \"{event.gift.extended_gift.name}\"")

    
    elif event.gift.gift_type != 1:
        print(f"{event.user.uniqueId} gửi cho chủ phòng \"{event.gift.extended_gift.name}\"")

@client.on("like")
async def on_like(event: LikeEvent):
    print(f"{event.user.uniqueId} gửi {event.likeCount} like cho chủ phòng ")
@client.on("follow")    
async def on_follow(event: FollowEvent):
    print(f"{event.user.uniqueId} vừa follow chủ phòng")
@client.on("share")
async def on_share(event: ShareEvent):
    print(f"{event.user.uniqueId} vừa share live ")   
@client.on('viewer_count_update')
async def on_connect(event:ViewerCountUpdateEvent):
    print(f"Lượt xem hiện tại là : {event.viewerCount}")
@client.on("mic_battle")
async def on_connect(event: MicBattleEvent):
    print(f"Trận PK đã bắt đầu với{', '.join([user.battleGroup.user.uniqueId for user in event.battleUsers])}")    
@client.on("emote")
async def on_connect(event: EmoteEvent):
    print(f"[EMOTE] {event.user.uniqueId} gửi nhãn dán : {event.emote.image.imageUrl}")   
@client.on("envelope")
async def on_connect(event: EnvelopeEvent):
    print(f"{event.treasureBoxUser.uniqueId} đã gửi {event.treasureBoxData}")   
@client.on("live_end")
async def on_connect(event: LiveEndEvent):
    print(f"Buổi live đã kết thúc :(")     


client.run()