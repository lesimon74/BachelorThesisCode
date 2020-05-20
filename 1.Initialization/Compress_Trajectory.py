u = Universe(pdb_, xtc_)
with Writer("6el6HoloEvery20thStep.xtc", u.atoms.n_atoms) as W:
    for ts in u.trajectory[::20]: #only every 20th step is written to new trajectory
        W.write(u)
