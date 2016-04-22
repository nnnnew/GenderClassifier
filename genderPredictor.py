import CSVReader
import random
from nltk import NaiveBayesClassifier
from nltk import classify


class genderPredict(object):

	def testAndTrain(self, trainingPercent = 0.60):
		featureset = self.getFeaturesSet()
		random.shuffle(featureset)
		name_count = len(featureset)
		cut_point = int(name_count*trainingPercent)

		train_set = featureset[:cut_point]
		test_set = featureset[cut_point:]
		
		self.train(train_set)

		return self.test(test_set)


	def getFeaturesSet(self):
		self.nameList = self._loadNames()
		return [(self._getFeatures(name), gender) for name, gender in self.nameList]

	def train(self, train_set):
		self.classifier = NaiveBayesClassifier.train(train_set)
		return self.classifier

	def test(self, test_set):
		return classify.accuracy(self.classifier, test_set)

	def getTrainSet(self):
		male_names = names.words('male.txt')
		female_names = names.words('female.txt')
		return ([(name, 'male') for name in male_name] + [(name, 'female') for name in female_name])

	def classify(self, name):
		feats = self._getFeatures(name)
		return self.classifier.classify(feats)

	def getMostInformativeFeatures(self, n=5):
		return self.classifier.most_informative_features(n)

	def _getFeatures(self, name):
		name = name.upper()
		return {
			'first_letter': name[0:1],
			'last_letter': name[-1:],
			'last_two': name[-2:],
			'last_three': name[-3:],
			'last_vowel': (name[-1:] in 'AEIOUY')
		}

	def _loadNames(self):
		return CSVReader.getNameList()

if __name__ == '__main__':
	gp = genderPredict()
	acc = gp.testAndTrain()
	while True:
		name = raw_input('Enter name to classify : ')
		print '%s is classified as %s\n' % (name, gp.classify(name))
	
	