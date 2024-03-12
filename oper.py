from .db import get_db
from flask import Blueprint,g,render_template,request,current_app


bp = Blueprint("oper", __name__, url_prefix="/oper")

@bp.route("/home")
def homepage():
    
    db_connection = get_db()

    with db_connection:
        with db_connection.cursor() as cursor:
            sql =  "SELECT * FROM sys_app_maintainer limit 30"
            cursor.execute(sql)
            maintainer_list = cursor.fetchall()
       
    print(maintainer_list)

    return render_template("oper/home.html",maintainer_list=maintainer_list)
    #return render_template("base.html")

@bp.route("/deploy")
def deploy():

    return render_template("oper/deploy.html")

@bp.route("/duty")
def duty():
    change_list=[{'changeid':"000001",'changename':'xxxx','changetype':'普通变更','status':'实施审批','status_desc':'变更审批','executor':'张豆', 'plan_starttime':'2024-02-29 21:00:00'},
                 {'changeid':"000001",'changename':'xxxx','changetype':'普通变更','status':'实施审批','status_desc':'变更审批','executor':'张豆', 'plan_starttime':'2024-02-29 21:00:00'},
                 {'changeid':"000001",'changename':'xxxx','changetype':'普通变更','status':'实施审批','status_desc':'变更审批','executor':'张豆', 'plan_starttime':'2024-02-29 21:00:00'},
                 {'changeid':"000001",'changename':'xxxx','changetype':'普通变更','status':'实施审批','status_desc':'变更审批','executor':'张豆', 'plan_starttime':'2024-02-29 21:00:00'},
                 {'changeid':"000001",'changename':'xxxx','changetype':'普通变更','status':'实施审批','status_desc':'变更审批','executor':'张豆', 'plan_starttime':'2024-02-29 21:00:00'},
                 {'changeid':"000001",'changename':'xxxx','changetype':'普通变更','status':'实施审批','status_desc':'变更审批','executor':'张豆', 'plan_starttime':'2024-02-29 21:00:00'},
                 {'changeid':"000001",'changename':'xxxx','changetype':'普通变更','status':'实施审批','status_desc':'变更审批','executor':'张豆', 'plan_starttime':'2024-02-29 21:00:00'},
     {'changeid':"000001",'changename':'xxxx','changetype':'普通变更','status':'实施审批','status_desc':'变更审批','executor':'张豆', 'plan_starttime':'2024-02-29 21:00:00'},
    {'changeid':"000001",'changename':'xxxx','changetype':'普通变更','status':'实施审批','status_desc':'变更审批','executor':'张豆', 'plan_starttime':'2024-02-29 21:00:00'},]
    
    duty_list=[{'department':'金融市场','daytime':'张豆 18618412857','nighttime':'邹锐 1867898776'},
               {'department':'公司金融','daytime':'张豆 18618412857','nighttime':'邹锐 1867898776'},
               {'department':'个人金融','daytime':'张豆 18618412857','nighttime':'邹锐 1867898776'},
               {'department':'运营清算','daytime':'张豆 18618412857','nighttime':'邹锐 1867898776'},
               {'department':'银行卡运营','daytime':'张豆 18618412857','nighttime':'邹锐 1867898776'},
               {'department':'核心银行','daytime':'张豆 18618412857','nighttime':'邹锐 1867898776'}
                 ]
    
    
    return render_template("oper/duty.html",change_list=change_list, duty_list=duty_list)

@bp.route("/tools")
def tools_repo():
    if current_app.config['online'] == "develop":
        return "show nginx page"
    else:
        return "show gitlab page"