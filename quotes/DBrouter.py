class AuthRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'auth',  }
    route_demo2_labels = {'app2', 'core2', 'demoapp2', 'myapp2'}

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_demo2_labels:
            return db == 'demo2'
        # elif app_label in self.route_app_labels:
        #     return db == 'demo2' and db == 'default'
        return None