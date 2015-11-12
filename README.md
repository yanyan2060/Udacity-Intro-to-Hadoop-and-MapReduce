# Udacity-Intro-to-Hadoop-and-MapReduce
<h1>Lesson 3 Problem Part 1 and Part 2</h1>
<h2>Final Project</h2>
Final Project: <p>P1:find for each student what is the hour during which the student has posted the most posts<br>
               p2:Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post.<br>
               p3:Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.<br>
               p4:writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.</p>
               
Useful command: hadoop fs -put txtname.txt<br>
                hadoop fs -ls<br>
                hadoop fs -tail txtname.txt<br>
                head -50 txtname.txt > test<br>
                cat test | ./mapper.py | sort | ./reducer.py
