'''
Example usage:
conda activate cox_lifelen_uvenal_melanom
python predict_existent.py -l1 0 -l2 1 -l3 3 -t1 0 -n1 0 -p1 0 -m1 0 -e1 0 -model_name ./CoxPHFitter_most_basic_on_cells_df.pickle'''
import click

@click.command()
@click.option('-l1' , help='лимфоциты вокруг опухоли степень (1,2,3)' , type=int)
@click.option('-l2' , help='лимфоциты в опухоли (степень - 1,2,3)' , type=int)
@click.option('-l3' , help='лимфоциты далко от узла (степень - 1,2,3)' , type=int)
@click.option('-t1' , help='тучные клетки вокруг опухоли (1,2,3)' , type=int)
@click.option('-n1' , help='нейтрофилы' , type=int)
@click.option('-p1' , help='плазмоциты' , type=int)
@click.option('-m1' , help='миелоидные клетки' , type=int)
@click.option('-e1' , help='эозинофилы' , type=int)
@click.option('-model_name' , help='версия модели' , default=1 , type=str)
def predict_survival( l1,l2,l3,t1,n1,p1,m1,e1, model_name ):
    #"""This script prints hello NAME COUNT times."""
    import pickle 
    import numpy as np
    with open(model_name, 'rb') as file:
        cph = pickle.load(file)
    print('model loaded')
    print('Fed arguments: ' , [l1,l2,l3,t1,n1,p1,m1,e1])
    
    #row_to_predict = pandas.DataFrame( [l1,l2,l3,t1,n1,p1,m1,e1] )
    row_to_predict = np.array([l1,l2,l3,t1,n1,p1,m1,e1])

    survival_predict = cph.predict_expectation(np.transpose(row_to_predict))
    survival_month = (survival_predict.unique()[0] / 30.44)
    int_month = int(survival_month)
    fractional_part = survival_month - int_month
    days = round(fractional_part * 30.44)
    answer = (int_month, days)
    return answer

if __name__ == '__main__':
    predict_survival()

