# Particle

This system has two interfaces. One for the writer to look into and another for the reader to view from. Particle is the writer interface and will be integrated into acme.

Also make sure you have rc, the plan9 shell
```bash
sudo dnf install rc #fedora
sudo apt install rc #debian, ubuntu
pkg install rc #termux
pkg_add rc #openbsd
```

If you do not have go installed refer here: https://go.dev/doc/install

If you do not want to use go and rc, see the bash dir. To ensure cross compatibility with time, basic bash verisions will be offered for particle.

In order to coordinate, there is a .ids.json file which is not git tracked

Todoist assumes you have TODOIST_KEY set in bashrc or kshrc

todoist: base todo interaction loop
assoc: layer on top of base todoist 
