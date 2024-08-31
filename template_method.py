class MachineModel(object):

    def __init__(self,X,y,model):

        '''Initiliazation feature and target variable'''
        self.X=X
        self.y=y
        self.X_train=None
        self.y_train=None
        self.X_test=None
        self.y_test=None
        self.model=model
        

    
    def data_cleaning_method(self):
        ''' Clean data'''
        raise NotImplementedError("Please Implement This Method")

    def data_spliting_method(self):
        '''Data spliting '''
        raise NotImplementedError("Please Implement This Method")

    def data_balance_method(self):
        ''' Making data balanced '''
        pass

    
    def data_scaling_method(self):
        ''' Scaling data'''
        pass

    
    def select_model(self,model):
        ''' Select machine learning model '''
        raise NotImplementedError("Please Implement This Method")

    
    def validation(self):
        ''' Validate ml_model'''
        raise NotImplementedError("Please Implement This Method")

    def model_score(self,use_hyperparameter=False):
        '''model score'''
        raise NotImplementedError("Please Implement This Method")
    
    def hyperparameter_tuning(self):
        '''Hyperparameter tuning '''
        pass


    def get_classification_report(self,use_hyperparameter=False):
        ''' Generate classification report'''
        pass

    def execute_all_method(self,scaling=False,balance=False):
        ''' Execute ml_pipeline method'''
        self.data_cleaning_method()

        if balance:
            self.data_balance_method()
        if scaling:
            self.data_scaling_method()
        self.data_spliting_method()
        self.select_model()
        self.validation()
        self.hyperparameter_tuning()



        

class SampleClassification(MachineModel):

    def __init__(self, X, y,model):
        super().__init__(X, y,model)

    def data_cleaning_method(self):
        print("data cleaned complete")

    def data_spliting_method(self):
        from sklearn.model_selection import train_test_split
        self.X_train,self.X_test,self.y_train,self.y_test=train_test_split(self.X,self.y)

    def select_model(self):
        self.model.fit(self.X_train,self.y_train)
        return self.model

    def model_score(self,use_hyperparameter=False):
        return self.model.score(self.X_test,self.y_test)


    def validation(self):
        from sklearn.model_selection import cross_val_score
        return cross_val_score(self.model,self.X,self.y,cv=5,n_jobs=-1)

    

if __name__=="__main__":
    import numpy as np

    from sklearn.linear_model import LogisticRegression

    from sklearn.neighbors import  KNeighborsClassifier
    X=np.random.randint(low=12,high=30,size=(100,2))
    y=np.random.randint(low=0,high=2,size=100)

    lg=KNeighborsClassifier(n_neighbors=5)

    s1=SampleClassification(X, y,model=lg)
    s1.execute_all_method()

    print(s1.model_score())



