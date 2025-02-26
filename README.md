# association_citation

Main Site(Github.io): <br> 
https://kaclark.github.io/association_citation/<br>

### Updates

This website was one idea long ago; it is undergoing rapid reconstruction!

For now, it is a guide to using the internet in my style.

If there's anything that I have taken a liking to it is style transfer, to breaking loose of the tempo of one song in order to jump out at the color another horizon promises...Computer Literacy and Mathematical Wonder will come to be one in time...

For the longest time I liked to read on my phone and I thought it was fun that a computer was in my pocket and that it could also be a library. I got a bit carried away with screenshotting over the years...but I would hate to lug around all those those images. I wanted the most concise way of storing the information I liked along the way, and that led to what this website wanted to be. But before it can be a place for experience it must put into play a method of gaining experience. 

For years I have grown more and more attached to the terminal interface associated with unix. However, those who created unix went on to make a graphical user interface embedded into the operating system itself. Unix was created as a programming environment. It was always already a refuge from the worst and grossest machinations of computers. Today we flee further from the operating system, but it could not be a better ally in our desire to expand our memory and our surface for the reception of beautiful movements of affect, passion, and spirit. 

### Suckless

To begin with let us replace the browser with something that sucks less. 

If you find yourself on linux, first let it be known that this breaks on gnome and that I had to find my way to xfce before it interface would even load properly

```
sudo dnf install surf #fedora 
sudo apt install surf #debian, ubuntu
```

If you do not want to use the package manager, you can try building from source

Maybe try (but be ready to debug)
```bash
git clone https://git.suckless.org/surf
cd surf
make clean install
```
See more here: https://git.suckless.org/surf/file/README.html

For a long time I used lynx, w3m, and a little bit of links. For a few days I plotted a life of only hget uri | htmlfmt in plan9, but netsurf there led me to surf here. Normal web things I would do from my phone browser can be done with surf. Replacing this is my first major computer goal of the season. 

```bash
surf https://bsky.app #login once then this works without signin!
surf https://kaclark.github.io/association_citation/
```

Association Citation will be revamped to work very well with surf.
Heads up, ctrl+shift+j/k to resize the zoom!

Okay so a few things I notice when I open up association citation
1. White and Bright!
2. Video Works!
3. PDFs do not work
4. The text in Spandakarika is much too large
5. The commentary and highlight text in the Leibniz page is perfect

So we can make this podcast forward, without a doubt. Video embedding will work well.
For video storage and server hosting, unlisted youtube videos embedded in the website html seem like the most straightforward option. Videos are just too large and if I am posting something on the internet like this I guess it can live on a Google Server without me getting the shivers...

I think I will tone the background color down. Maybe make a dark mode and have a button somewhere for switching between light and dark mode?

Now the next thing to rejoice over after the suckless surf browser is the typesetting that existed before tex and latex. Algorithms, partially ordered sets, and clean homework are all great, but at AT&T troff was all the rage. Why do we have PDFs? Because the printers traded off with the CPUs; workload moved over to the PC and we got those documents. I wish to provide documents in the smallest footprint possible over radio waves. I never intend to print this text. PDFs are overkill. Manuscripts in the .ms format can be converted to pdf, html, and terminal output with ease with plan9 tools. My output will be very slow for some time as I work on setting up a system for cranking out manuscripts, but I assure the reader that a veritable printing press is on its way...

When one reads the documentation of bsky, it becomes clear that a filesystem system would fare well, and where else do we find the best example of this but plan9 and its manifold derivatives? Go Glenda Go...

What does .com mean? It was first .commerical in some sense. It was only after the onslaughts of speculation then died down that .com relaxed and anyone could get one. I was born after the wreckage to laid waste to the dreams of yesterday, so I never got this impression. Oh how shocking to gain the distance of age and to reckon higher recognition of the past tragedies which have inscribed the common details of my daily life in their boring manifestation.

Java, a language I learned first above all beyond CSS, html, and LabVIEW, was the accursed murderer of that wonderous demiurge InfernoOS after Plan9. Inferno brought us portable code, always in limbo: written once and ran everywhere...my first command line interface memories are compiling what? Java...before I learned python did I not also slip in some JavaScript? The crime redoubled...in my web browsing days in those unix terminal haunts I did everything to evade this scourge JavaScript...and now with surf we find a way to approach it without the bloat which has become common purchase today. The git repo listed above is a study in excellence. It humbles me and I shall build my website to be held through its gaze!  

### A Second Word on Browsers

While surf was something of a revelation to me, I must admit that there are others in its class and that I would do well to write my own in time. I have found that there is a vim like browser known as qutebrowser, and it seems more featured than the surf browser and I am more immersed within this browser. It seems to run well in every condition I test it. The suckless culture is an intense one, and it is alluring though maybe too hardcore. I seek to only really write C when reading Plan9 source code, if I can be spared any other horrors. Maybe qutebrowser could be rewritten somehow to work well with pypy and goless with concurrent processing motivating every algorithm and movement of data -- after Chemistry has been invested with the Crown of Computer Science.

### Chemistry as the Queen of Computer Science

In my pocket I carry a post-unix operating system which has been bent and contorted in various ways. Google came into possession of android and such a linux device was shaped according to their desire. Over time, termux came about and with it an extension of the unix philosophy made accessible to the android user a programming environment. We must remember that after Multics, those at Bell Labs used the Digital Equipment Corporations PDP machines in order to build a programming environment to their liking: UNIX. These experimentations soon led to the C programming language.  

Today I write mostly in python. I have seen the great vigor that rust moves with today, and I see that it will soon overtake C -- or so the heralds of compiler eschatology cry. Go, however, has something of those Bell Labs Technians' experiences inscribed into it. It was initially compiled with plan9 C, so the legends go. In a much less elegant manner, python is usually involved with C. Pypy, however, is python moved through python. If one seeks concurrency, that theoretical intervention which stands to differentiate Plan9 and Inferno from UNIX, then fragments of the history between C and python lock one out of paradise. In order to go beyond this and to reach for the alluring brilliance of concurrency, we should rather have to abandon that baggage of C with python. Pypy answers these prayers. Go primitives were made for python in the package goless, and it was designed with pypy in sight among other implementations of the language. 

In many cases, I use python as a binding to libraries designed in this and that language. I do not know if pypy can handle that, but I have simple desires with the use of pypy and goless -- if it can be done, for I must test it and see it go boom before I can endow it with transcendental mania -- which delimit themselves to the construction of models for molecular systems. If it can be said that in the UNIX philosophy that everything is a file, then we must hark with heed the format of chemical files which allow us to submit a string of ascii characters which can be interpreted as the chemicals we take to drawing on blackboards and paper through the library openbabel. For example we need only endeavor thus:

```bash
sudo dnf install openbabel
obabel -:"c1cc(C=O)ccc1C(=O)O" -O out.svg --genalias -xA
```

Further investigations regarding both the .smi files for SMILES as the standard is outline here http://opensmiles.org/opensmiles.html are to be undertaken. Reference to .smi files from pypy goless channels in order to write models of molecular systems would be an excellent place to begin a computational chemistry of literate programming. It was said by the one who forged tex that the programmer must write for other humans. If I wanted to write for the machines, I would lose the fellow being. Communication must be struggled for at the interface of the systems that the engineers composes and investigates. Intellect which cannot be shared so easily is of low rank and of little majesty. Nous is an ever recursive bounty. The chemist for too long has taken to blackboards and paper and not the teletype interface. Electronics forged these technologies, and yet those who study those intimate dances of the electrons shy away from their rightful throne and altar: the filesystem and its concurrent interface. 

On this question of modelling we are to test the living language by putting into motion what is said here: doi:10.1016/j.tcs.2004.03.066

To offer the reader a glimpse of the sheer sublime awe we are before, let us offer the copypasta:

We use the pi-calculus to model the evolution of biochemical systems, taking advantage of their similarities with global computation applications. First, we present a reduction semantics for the pi-calculus from which causality and concurrency can be mechanically derived. We prove that our semantics agrees with the causal definitions presented in the literature. We also extend our semantics to model biological compartments. Then, we show the applicability of our proposal on a couple of biological examples.

A network of proteins can be seen as a computing machinery, made of processing agents that cooperate to achieve a common goal. Agents autonomously compute on their own and exchange information each other [51]. This informal description applies as well to concurrent system, that are made of large number of geographically dispersed, possibly mobile and communicating computing agents. This paradigm is now-a-days called global computing. Process calculi are the most popular formalism to describe and study global computing applications. One of the most popular process calculi is the pi-calculus [39]. Regev et al. [52] were the first to use the pi-calculus as a model of biochemical processes, taking advantage of similar experiences in the Petri net -eld[17,18,20] and on the results from process calculi for mobility. They model reactants as pi-calculus processes and biochemical reactions as communications. The authors claim that the pi-calculus permits to better integrate dynamics, molecular and biochemical details. Further work lead to a more precise model [47], based on the stochastic pi-calculus [45], an extension of the original calculus with probabilistic distributions that govern the race conditions. So, also quantitative aspects of reactions can be taken into account. Besides the study of quantitative aspects like the one mentioned above, the literature on concurrency has many proposals on the description of the causal relations between the activities that agents perform, as well as of the relation of independence between actions (concurrency). According to its supporters, causality permits more accurate representations of the behaviour of concurrent systems than classical interleaving representations; in particular, causality seems to play a relevant role in understanding complex biochemical pathways. Also, a single causal representation describes all the behaviour in which independent activities are temporally linearized, thus offering a more concise model. In this paper we offer such a causal extension of the pi-calculus, and we apply it to a couple of biological examples.
