import pandas as p
import time
start_time = time.clock()
dataset = p.read_csv('movie_metadata.csv');
actors1 = set(dataset.actor_1_name.unique())
actors2 = set(dataset.actor_2_name.unique())
actors3 = set(dataset.actor_3_name.unique())
actors = set()
actors = actors1.union(actors2.union(actors3))
actors_imdb = {}
for x in actors:
	actors_imdb[x] = 0
for a in dataset.iterrows():
	if(a[1].imdb_score>7):
		actors_imdb[a[1].actor_1_name] = actors_imdb[a[1].actor_1_name] + 3;
		actors_imdb[a[1].actor_2_name] = actors_imdb[a[1].actor_2_name] + 3;
		actors_imdb[a[1].actor_3_name] = actors_imdb[a[1].actor_3_name] + 3; 
	elif(a[1].imdb_score>6):
		actors_imdb[a[1].actor_1_name] = actors_imdb[a[1].actor_1_name] + 2;
		actors_imdb[a[1].actor_2_name] = actors_imdb[a[1].actor_2_name] + 2;
		actors_imdb[a[1].actor_3_name] = actors_imdb[a[1].actor_3_name] + 2;
	elif(a[1].imdb_score>5):
		actors_imdb[a[1].actor_1_name] = actors_imdb[a[1].actor_1_name] + 1;
		actors_imdb[a[1].actor_2_name] = actors_imdb[a[1].actor_2_name] + 1;
		actors_imdb[a[1].actor_3_name] = actors_imdb[a[1].actor_3_name] + 1; 
imdb_actors = {}
imdb = set()
for x in actors_imdb:
	imdb_actors[actors_imdb[x]] = []
	imdb.add(actors_imdb[x])
for x in actors_imdb:
	l = imdb_actors[actors_imdb[x]]
	l.append(x)
imdb_list = []
for x in imdb:
	imdb_list.append(x)
print "Top 10 actors giving hit(rated according to imdb_score)"
c=1;
for x in reversed(imdb_list):
	if(c>10):
		break;
	for y in imdb_actors[x]:
		print y
	c = c+1	
print time.clock()-start_time," seconds"
