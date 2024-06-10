import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from database.connection import get_db_connection
from database.setup import create_tables

conn = get_db_connection()
cursor = conn.cursor()
class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        if not isinstance(name, str) or(2<= len(name)>= 16) :
            raise ValueError("name should be a string and  between 2 - 16")
        self._name = name
        self._category = category
        self.save()

    def __repr__(self):
        return f'<Magazine {self.name}>'
    def save (self):
        cursor.execute("SELECT id FROM magazines WHERE id = ?", (self._id,))
        if cursor.fetchone():
                raise ValueError(f"Article with id {self._id} already exists")
        sql = """
         INSERT INTO magazines (
         id, name, cartegory)  
         VALUES (?, ?, ?)  
        """
        cursor.execute(sql,(self._id, self._name, self._category))
        conn.commit()

    def articles(self):
        query = """
              SELECT articles.title
              FROM articles
              LEFT JOIN magazines
              on articles.magazine_id = magazines.id
              WHERE magazines.id = ?

        """
        cursor.execute(query, (self._id,))
        articles = cursor.fetchall()
        return [article[0] for article in articles] if articles else None
    def contributors(self):
        query = """
          SELECT authors.name
          FROM authors
          LEFT JOIN articles
          ON authors.id = articles.author_id
          LEFT JOIN magazines
          ON articles.magazine_id = magazines.id
          WHERE magazines.id = ?
        """
        cursor.execute(query, (self._id,))
        contributors = cursor.fetchall()
        return [contributor[0] for contributor in contributors] if contributors else None

        
    @property
    def name(self):
        return self._name
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if not isinstance (id , int):
            raise   TypeError("id must be an integer")
        self._id = id

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value    


        