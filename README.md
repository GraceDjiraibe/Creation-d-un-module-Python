# Creation-d-un-module-Python

Le but de ce script consiste à chercher des gènes à partir de 6 cadres de lectures différents à partir d'un fragment du chromosome I de la levure Saccharomyces cerevisiae. 
 
On rappelle succinctement la notion de cadre de lecture. Soit la séquence d’ADN suivante
5'-CTCTAGATAGCTCCG... -3' que l’on lit dans le sens classique 5’ ! 3’. Etant donné que la séquence
est lue par paquets de 3 nucléotides (chaque paquet de 3 correspond à un codon), on peut
lire cette séquence soit en commençant au nucléotide 1, soit en commençant au nucléotide 2, soit en
commençant au nucléotide 3.

Le cadre de lecture 1 commence au nucléotide 1, puis on lit la séquence par paquets de 3. De même, le
cadre de lecture 2 commence au nucléotide 2, puis on lit la séquence par paquets de 3. Enfin, le cadre
de lecture 3 commence au nucléotide 3, puis on lit la séquence par paquets de 3.

cadre 1 : 5' CTC TAG ATA GCT ... -3'
cadre 2 : 5' TCT AGA TAG CTC ... -3'
cadre 3 : 5' CTA GAT AGC TCC ... -3'


Le script à été découpé en plusieurs fonctions.


Afin de créer ce script nous avons besoin des fichier suivants : 

- "genetic_code.txt" contenant 2 colonnes avec le code génétique (première colonne représentant les codons, la deuxième colonne représentant les acides aminés, l'étoile veut dire codon stop).
- "debut_chromI_Sacch_Crev.fna" qui contient une portion de la séquence du chromosome I de la levure Saccharomyces cerisaie.
