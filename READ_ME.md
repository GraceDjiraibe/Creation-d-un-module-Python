Le but de ce script consiste à chercher des gènes à partir de 6 cadres de lectures différents à partir d'un fragment du chromosome I de la levure Saccharomyces cerevisiae. 
 
On rappelle succinctement la notion de cadre de lecture. Soit la séquence d’ADN suivante

Le cadre de lecture 1 commence au nucléotide 1, puis on lit la séquence par paquets de 3. De même, le

cadre 1 : 5' CTC TAG ATA GCT ... -3'


Le script à été découpé en plusieurs fonctions.


Afin de créer ce script nous avons besoin des fichier suivants : 

- "genetic_code.txt" contenant 2 colonnes avec le code génétique (première colonne représentant les codons, la deuxième colonne représentant les acides aminés, l'étoile veut dire codon stop).
- "debut_chromI_Sacch_Crev.fna" qui contient une portion de la séquence du chromosome I de la levure Saccharomyces cerisaie.