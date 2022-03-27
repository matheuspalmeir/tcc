
class My_Model:

	def __init__(self):
		self.collection = {}
		self.earth_truth = {}
		# self.collection['dim'] = {'width' : 2665, 'height': 2665}
		# self.earth_truth['dim'] = {'width' : 2665, 'height': 2665}
		self.data_train = []
		self.data_target = []
		self.path = 'images/Nov_2015/'
		self.files_name = [
			'20151111_merge_B1_cut.tif',
			'20151111_merge_B2_cut.tif',
			'20151111_merge_B3_cut.tif',
			'20151111_merge_B4_cut.tif',
			'20151111_merge_B5_cut.tif',
			'20151111_merge_B6_cut.tif',
			'20151111_merge_B7_cut.tif'
		]
		self.path_target = 'images/earth_truth/'
		self.file_target = '20151111_merge_B1_cut_raster.tif'


	def __getCollectionsByIndex__(self, index):
		return self.collection[index]

	def __getCollection__(self):
		return self.collection

	def __getDataTrain__(self):
		return self.data_train

	def __getDataTarget__(self):
		return self.data_target

	def __getEarthTruth__(self):
		return self.earth_truth
	
	def __setEarthTruth__(self, index, data):
		self.earth_truth[index] = data

	def __setCollection__(self, index, data):
		self.collection[index] = data 

	def __setDataTarget__(self, data):
		self.data_target = data


