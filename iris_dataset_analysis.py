
'''
Iris is a flower, so this dataset contains the data about the
flowers to classify it.

The Iris dataset contains 5 columns, each describing a different attribute of Iris flowers:

sepal length (cm): The length of the sepal of the iris flower, measured in centimeters.
sepal width (cm): The width of the sepal of the iris flower, measured in centimeters.
petal length (cm): The length of the petal of the iris flower, measured in centimeters.
petal width (cm): The width of the petal of the iris flower, measured in centimeters.
species: The species of the iris flower, which can be one of three types: Setosa, Versicolor, or Virginica.
'''
import seaborn as sns
import matplotlib.pyplot as plt

data = sns.load_dataset('iris')

fig, axes = plt.subplots(3,3, figsize=(10,6))

# Matplot lib charts
axes[0,0].scatter(data['sepal_length'], data['sepal_width'], 
                  c='gold',
                  edgecolors='black')
axes[0,0].set_title('Scatter plot analysis')


# Seaborn charts
sns.histplot(data=data,x="sepal_width", hue='sepal_width', 
             legend=False, ax=axes[0,2])
axes[0,2].set_title('Histogram plot analysis')

sns.lineplot(data=data, x='sepal_length', y='sepal_width', ax=axes[0,1])
axes[0,1].set_title('Line plot analysis')

sns.barplot(x="species",y='sepal_length',
            data=data, ax=axes[1,0], color='green',
            errcolor='red')
axes[1,0].set_title('Bar plot analysis')

sns.stripplot(data=data,x="species", y='sepal_width',
             hue_order='species', color='gold', ax=axes[1,1])
axes[1,1].set_title('Strip plot analysis')

sns.swarmplot(data=data,x="species", y='sepal_width',
             hue_order='species', color='red', ax=axes[1,2])
axes[1,2].set_title('Swarm plot analysis')


sns.countplot(x="species",
            data=data, ax=axes[2,0], hue='species')
axes[2,0].set_title('Count plot analysis')

sns.boxplot(data=data,x="species", y='sepal_length',
             hue_order='species',color='gold', ax=axes[2,1])
axes[2,1].set_title('Box plot analysis')


sns.set_theme(context='paper', style='darkgrid')
sns.violinplot(data=data,x="species", y='sepal_width',
             hue_order='species', color='gold', ax=axes[2,2])
axes[2,2].set_title('Violin plot analysis')

font1 = {'family':'serif','color':'blue','fontsize':20}

plt.suptitle('Iris whole data analysis',fontdict=font1)
plt.tight_layout(h_pad=0.4,w_pad=0.5)
plt.show()