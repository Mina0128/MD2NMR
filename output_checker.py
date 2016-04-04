import os

orig_filenames = os.listdir(os.getcwd() + '/koes/')

new_filenames = os.listdir(os.getcwd() + '/output/')

for i in range(0, len(new_filenames)):
	print '\nChecking: ' + new_filenames[i]
	orig = [line.rstrip('\n') for line in open(os.getcwd() + '/koes/' + orig_filenames[i])]
	new = [line.rstrip('\n') for line in open(os.getcwd() + '/output/' + new_filenames[i])]

	for j in range(0, len(new_filenames)):
		# Split on the first '|'
		orig_hold = orig[j].split('|', 1)
		new_hold = new[j].split('|', 1)

		# For debugging
		# print '\n\nOriginal output line: ' + str(orig_hold)
		# print 'New output line: ' + str(new_hold)

		# Split that separates frame number and the distances
		orig_frame_and_dist = orig_hold[1].split('|', 1)
		new_frame_and_dist = new_hold[1].split('|', 1)

		# Output what frame number is being checked
		orig_frame_num = orig_frame_and_dist[0]
		new_frame_num = new_frame_and_dist[0]
		print '\nFrame #: ' + new_frame_num

		# Check for atom pattern
		orig_atom_pattern = orig_hold[0].split(':')
		new_atom_pattern = new_hold[0].split(':')

		if len(orig_atom_pattern) == len(new_atom_pattern):
			for a in range (0, len(orig_atom_pattern)):
				if orig_atom_pattern[a] == new_atom_pattern[a]:
					continue
				else:
					print "Wrong atom pattern: " + orig_atom_pattern[a] + " and new output has " + new_atom_pattern[a]
		else:
			print "Wrong atom pattern: " + str(orig_atom_pattern) + " new output has " + str(new_atom_pattern)

		# Compare distances
		orig_dists = orig_frame_and_dist[1].split('|')
		new_dists = new_frame_and_dist[1][:-1].split('|')

		if len(orig_dists) == len(new_dists):
			for d in range(0, len(new_dists)):
				if orig_dists[d][:4] == new_dists[d][:4]:
					continue
				else:
					print "Wrong distance, original: " + orig_dists[d] + " new: " + new_dists[d]
		else:
			print "Wrong distances, original has: " + str(orig_dists) + " new output has " + str(new_dists)
