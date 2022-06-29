import ldap3
def verification_ad(LDAP_SERVER_IP,LDAP_SERVER_NAME,LDAP_USER,LDAP_PSW):
    server = ldap3.Server(LDAP_SERVER_IP,port=389,get_info=ldap3.ALL)
    try:
        # conn = ldap3.Connection(server,user="{}\\{}".format(LDAP_SERVER_NAME,LDAP_USER), password=LDAP_PSW,auto_bind=True,authentication='NTLM')
        conn = ldap3.Connection(server,user=("%s\\%s"% (LDAP_SERVER_NAME,LDAP_USER)), password=LDAP_PSW,auto_bind=True,authentication='NTLM')
        # print(u"lian jie cheng gong\n")
        from XYYScript import maya_menu
        return "lian jie cheng gong"
    except Exception as e:
        print(u'wu fa lian jie\n')