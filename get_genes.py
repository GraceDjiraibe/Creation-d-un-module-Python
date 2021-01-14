
__authors__ = ("Grace Djiraibe")
__version__ = "1.0.0"
__date__ = "18/06/2020"


BASE_COMP = {"A":"T","T":"A","G":"C","C":"G"}


def read_genetic_code(filename):
	""" Fonction qui renvoie un dictionnaire du code génétique.

	PARAMETRE
	---------
	* filename: str
		Nom du fichier contenant 2 colonnes avec le code génétique.

	RETOUR
	------
	* genetic_code: dict
		Dictionaire du code génétique.
	"""
	genetic_code = {}
	with open(filename, 'r') as gene_file:
		for ligne in gene_file:
			codon, prot = ligne.split()
			genetic_code[codon] = prot
	return genetic_code
 
def read_seq(filename):
	""" Fonction qui lit le fichier passer en arguments et renvoie le contenu
		sous forme de string.

	PARAMETRE
	---------
	* filename: str
		Nom du fichier passer en argument (fichier fasta).

	RETOUR
	------
	* sequence: str
		Séquence de nucléotides extraite du fichier fasta passser en argument
	"""
	sequence = ""
	with open(filename, 'r') as fasta_file:
		for ligne in fasta_file:
			if not ligne.startswith(">"):
				sequence += ligne.strip()
	return sequence

def translate(gene, genetic_code):
	""" Fonction qui permet de traduire les elements de la sequence de nuclétotide à partir 
		du dictionnaire qui a pour clé les codons et valeurs les correspondant aux protéines. 

	PARAMETRE
	---------
	* gene: str
		Sequence de gène issue du fichier fasta.
	* genetic_code: dict
		Dictionnaire contenant les codons en tant que clé et la protéine correspondante 
		en tant que valeur.
	* cadre: int
		Origine du cadre de lecture, permet de décaler la fenêtre de lecture.

	RETOUR
	------
	* seq_prot: str
		Séquence protéique traduite à partir de la séquence d'adn.
	"""
	seq_prot = ""
	for i in range(0,len(gene)+1,3):
		codon = gene[i:i+3]
		print(codon)
		if codon in genetic_code and genetic_code[codon] != "*":
			seq_prot += genetic_code[codon]
		else:
			seq_prot += genetic_code[codon]
			break
	return seq_prot

def find_genes(seq, num_codon_start):
	gene = seq[num_codon_start:]
	return gene 

def find_all_genes(filout, seq, genetic_code):
	""" Trouve tous les gènes et les imprimme dans une fichier de sortie.

	PARAMETRE
	---------
	* filout :str 
		fichier de sortie avec les genes et informaitons.
	* seq : str
		La séquence d'adn.
	* genetic_code : dict
		Dictionnaire contenant les codons en tant que clé et la protéine correspondante 
		en tant que valeur.
	* brin : str
		Direct ou complementaire 
	"""
	with open(filout,'w') as file_sortie:
		cadre = [0,1,2] # Cadre de lecteure de la séquence 
		for j in range(len(cadre)):
			for i in range(0, len(seq)+1,3):
				if seq[i:i+3] == "ATG":
					pos = i 
					gene = find_genes(seq,pos)
					proteine = translate(gene,genetic_code)
					file_sortie.write(" cadre de lecture {} \t indice debut {} \t indici sortie {} \t sequence {} \t proteine {}\n".format\
					(cadre[j],i,len(gene)-1,gene,proteine) )
				

def seq_comp_inverse(seq):
	""" Donne la sequence coplementaire inverse de l'adn.

	PARAMETRE
	---------
	* seq : str
		Sequence d'adn."""
	seq_comp_inv = []
	for base in seq:
		seq_comp_inv.append(BASE_COMP[base])
		seq_comp_inv.reverse()
	return "".join(seq_comp_inv) 



	


if __name__ == "__main__":
	# 1) Recup code genetique (dico) à partir du fichier "genetic_code.txt"
	file_dico = "genetic_code.txt"
	dico = read_genetic_code(file_dico)

	# 2) Recup seq genome (string) à partir du fichier "debut_chromI_Sacch_Cerev.fna"
	# (appel fonction read_seq()).
	file_genome = "debut_chromI_Sacch_Cerev.fna"
	sequence = read_seq(file_genome)

	# 3) Generation seq inverse complementaire.
	seq_compl = seq_comp_inverse(sequence)

	# 4) Ouverture fichier output "sortie.txt".
	sortie = "result.txt"

	find_all_genes(sortie,sequence,dico)
	

