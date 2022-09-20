
##################***************************************     community extra settings     ***************************************##################

from arango import ArangoClient

client = ArangoClient(hosts="http://localhost:8529")
db = client.db("community",username="root",password="postgres")


if db.has_graph("community"):
    my_community = db.graph("community")
else:
    my_community = db.create_graph("community")

if db.has_graph("follow_people"):
    follow_people = db.graph("follow_people")
else:
    follow_people = db.create_graph("follow_people")


if db.has_graph("accepted_request"):
    accepted_people = db.graph("accepted_request")
else:
    accepted_people = db.create_graph("accepted_request")


if db.has_graph("posts"):
    post_create = db.graph("posts")
else:
    post_create = db.create_graph("posts")


if db.has_graph("givelike"):
    give_like = db.graph("givelike")
else:
    give_like = db.create_graph("givelike")


if db.has_graph("givecomment"):
    give_comment = db.graph("givecomment")
else:
    give_comment = db.create_graph("givecomment")


if db.has_graph("page"):
    page = db.graph("page")
else:
    page = db.create_graph("page")


if db.has_graph("share_post_to_page"):
    share_post_to_page = db.graph("share_post_to_page")

else:
    share_post_to_page = db.create_graph("share_post_to_page")

if db.has_graph("report_post"):
    report_post = db.graph("report_post")
else:
    report_post = db.create_graph("report_post")

if db.has_graph("page_invitation"):
    page_invitation = db.graph("page_invitation")
else:
    page_invitation = db.create_graph("page_invitation")

if db.has_graph("event_invite"):
    event_invite = db.graph("event_invite")
else:
    event_invite = db.create_graph("event_invite") 

# group
if db.has_graph("group"):
    group = db.graph("group")
else:
    group = db.create_graph("group")

if db.has_graph('user_setting'):
    user_setting = db.graph('user_setting')
else:
    user_setting = db.create_graph('user_setting')

