import postgresql
import csv
from diagrams import Cluster, Diagram
from diagrams.aws.database import RDS

host = 'xx'
user= 'xx'
passw = 'xx'
port = xx
dbname = 'xx'


def save_job_precedent_to_csv():
	"""
	This funcion read job_precedent from POSTGRESQL and save it in a csv file
	I created this function because I do not want to connect to postgres every time I run the script, job_precedent table is not updated too frecuently

	"""

	db = postgresql.open(f'pq://{user}:{passw}@{host}:{port}/{dbname}')
	jobs = db.prepare("SELECT a.* from pr_wrk.load_precedent a inner join pr_wrk.load_parameters b on a.job_cd=b.job_cd where b.productive_ind=1")


	with open("jobs_precedent.csv", mode='w') as jobs_precedent_file:
		jobs_writer = csv.writer(jobs_precedent_file, delimiter=',')

		for job in jobs:
			jobs_writer.writerow(job)


def read_job_precedent_csv():

	"""
	This funcion read job_precedent csv file and return a list
	FORMAT [['JOB','PRECEDENT'], ['JOB','PRECEDENT'], ['JOB','PRECEDENT'], ....]
	
	"""

	jobs_lst = []

	with open("jobs_precedent.csv", mode='r') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		for row in csv_reader:
			jobs_lst.append(row)
			

	return jobs_lst


def draw_job_precedent(updateCsv= False):

	# if updateCsv parameters is True , i update csv file
	if updateCsv: save_job_precedent_to_csv()
	# reading csv file and saving list into jobs_lst
	jobs_lst = read_job_precedent_csv()

	# initializating diagram objects dictionary
	nodes_dict = {}

	# creating diagram
	with Diagram("JC - DataPipeline_log", direction = "TB"):

		# initializating connections list
		relationships = []
		

		jobs_lst = sorted(jobs_lst, key = lambda x: x[0])

		for jobs in jobs_lst:

				# Extracting job name
				job = '_'.join(jobs[0].split('_')[:2])
				# Extracting precedent job name
				precedent_job = '_'.join(jobs[1].split('_')[:2])

				#print(job, precedent_job)

				# Checking if I already created the job's node
				if job not in nodes_dict:
					nodes_dict[job] = RDS(job)
				# Checking if I already created the precendet job's node
				if precedent_job not in nodes_dict:
					nodes_dict[precedent_job] = RDS(precedent_job)

				# Adding the connection between both jobs
				relationships.append(nodes_dict[job] << nodes_dict[precedent_job])

	return True

draw_job_precedent()
