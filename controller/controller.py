import sys
sys.path.append('.')
import requests
from model.model import Model


class Controller(Model):

    ############################ INSERTION A LA BASE DE DONNÉES ##################### 
    @classmethod
    def insert_data(cls,users,query):
        try:
            for add in users:
                cls.cursor.execute(query,add)
            cls.db.commit()
        except Exception as e:
            print(e)

    @classmethod
    def rollback(cls):
        try:
            cls.curseur.execute("SHOW TABLES")
            table = input('Entrer la table à vider\n')
            cls.curseur.execute(f"TRUNCATE TABLE {table}")
            cls.db.commit()
        except Exception as e:
            print("mauvais choix")


    ############################# RECUPERE TOUS LES ELEMENTS DE LA TABLE #############
    @classmethod
    def all(cls):
        table = input('Entrer la table\n')
        cls.curseur.execute(f"SELECT * FROM {table}")
        results = cls.curseur.fetchall()
        for result in results:
            print(result)

    # RECUPERATIONS
    def get_elementApi(table):
        url = f'https://jsonplaceholder.typicode.com/{table}'
        responses = requests.get(url)
        vues = responses.json()
        return vues


    # Recuperer des éléments du API
    users = get_elementApi('users')
    todos = get_elementApi('todos')
    photos = get_elementApi('photos')
    albums = get_elementApi('albums')
    comments = get_elementApi('comments')
    company = get_elementApi('company')
    address = get_elementApi('address')

    def recuper_user(users):
        for vue in users:
            id =vue.get('id')
            name =vue.get('name')
            username=vue.get('username')
            email=vue.get('email')
            phone=vue.get('phone')
            website=vue.get('website')
            street=vue["address"]['street']
            suite=vue["address"]['suite']
            city=vue["address"]['city']
            geo=str(vue["address"]['geo'])
            # print(geo)
            datas = Controller()
            users = [
                {
                    'id':id,
                    'name':name,
                    'username':username,
                    'email':email,
                    'phone':phone,
                    'website':website,
                    'street':street,
                    'suite':suite,
                    'city':city,
                    'geo':geo
                }
            ]
            try:
                datas.insert_data(users,
                "INSERT INTO users(id,name,username,email,phone,wesite,street,suite,city,geo) VALUES(%(id)s,%(name)s,%(username)s,%(email)s,%(phone)s,%(website)s,%(street)s,%(suite)s,%(city)s,%(geo)s")
            except Exception as e:
                print(e)



    def recuper_posts(posts):
        for vue in posts:
            userid = vue.get('userId')
            id = vue.get('id')
            title = vue.get('title')
            body = vue.get('body')

            posts = [
                {
                    'userId':userid,
                    'id':id,
                    'title':title,
                    'body':body
                }
            ]

            datas = Controller()
            try:
                datas.insert_data(posts,
                "INSERT INTO post(userId,id,title,body) VALUES(%(userId)s,%(id)s,%(title)s,%(body)s")
                
            except Exception as e:
                print(e)
    # recuper_posts(posts)

    def recuper_todos(todos):
        for vue in todos:
            userid = vue.get('userId')
            id = vue.get('id')
            title = vue.get('title')
            todos = [
                {
                    'userId':userid,
                    'id':id,
                    'title':title
                }
            ]
            datas = Controller()
            try:
                datas.insert_data(todos,
                "INSERT INTO todos(userId,id,title) VALUES(%(userId)s,%(id)s,%(title)s")
            except Exception as e:
                print(e)

    # recuper_todos(todos)

    def recuper_photos(photos):
        for vue in photos:
            albumId      = vue.get('albumId')
            id           = vue.get('id')
            title        = vue.get('title')
            url          = vue.get('url')
            thumbnailUrl = vue.get('thumbnailUrl')

            photos = [
                {
                    'albumId':albumId,
                    'id':id,
                    'title':title,
                    'url':url,
                    'thumbnailUrl':thumbnailUrl
                }
            ]
            datas = Controller()
            try:
                datas.insert_data(photos,
                "INSERT INTO photos(albumId,id,title,url,thumbnailUrl) VALUES(%(userId)s,%(id)s,%(title)s,%(thumbnailUrl)s")
                
            except Exception as e:
                print(e)
    # recuper_photos(photos)
            
        
