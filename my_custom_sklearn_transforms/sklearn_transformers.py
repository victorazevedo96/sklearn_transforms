from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class Faz_Tudo(BaseEstimator, TransformerMixin):
    def __init__(self, colunas):
        self.columns = colunas

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        data = data.drop(columns=['INGLES'],axis=1)
        ingles = pd.DataFrame(data=X['INGLES'])
        data =  data.drop(labels = self.colunas,axis=1)

        si = SimpleImputer(
        missing_values=np.nan,  # os valores faltantes são do tipo ``np.nan`` (padrão Pandas)
        strategy='mean',  # a estratégia escolhida é a alteração do valor faltante por uma constante
        verbose=0,
        copy=True
    )
        si.fit(X=data)
        data_return = pd.DataFrame.from_records(data=si.transform( X=data),columns=data.columns)

        si_ingles = SimpleImputer(
        missing_values=np.nan,  # os valores faltantes são do tipo ``np.nan`` (padrão Pandas)
        strategy='most_frequent',  # a estratégia escolhida é a alteração do valor faltante por uma constante
        verbose=0,
        copy=True
        )
        si_ingles.fit(X=ingles)
        ingles = pd.DataFrame.from_records(data=si_ingles.transform(X=ingles),columns=['INGLES'])

        data_return['INGLES'] = ingles
