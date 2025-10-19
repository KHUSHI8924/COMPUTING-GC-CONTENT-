import matplotlib.pyplot as plt
def calculate_gc_content(dna):
    dna=dna.upper().strip()
    total=len(dna)
    if total==0:
        return{"G%":0, "C%":0,  "GC%":0}
    
    g_count=dna.count('G')
    c_count=dna.count('C')
    
    g_percent= (g_count/total) *100
    c_percent= (c_count/total) *100
    gc_percent= g_percent+c_percent
    
    return{"G%":g_percent, "C%":c_percent, "GC%":gc_percent}

def plot_gc_content(dna):
    gc_data=calculate_gc_content(dna)
    
    labels=list(gc_data.keys())
    values=list(gc_data.values())
    
    plt.figure(bitsize=(6,4))
    bars=plt.bar(labels,values)
    
    bars[0].set_colour('green')
    bars[1].set_colour('blue')
    bars[2].set_colour('violet')
    
    plt.title("GC Content analysis of DNA sequence",fonts=14)
    plt.label("Percentage(%)", fonts=12)
    plt.lim(0, 100)
    
    # Add value labels above bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 1, f'{height:.2f}%', ha='center', va='bottom', fonts=10)

    plt.tight_layout()
    plt.show()


# Example DNA sequence
dna_sequence = "AGCTATAGCGGCGC"
plot_gc_content(dna_sequence)
    

    
    
    