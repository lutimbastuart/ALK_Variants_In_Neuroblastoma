# Define selections for the two protein chains
# Replace "chain A" and "chain B" with your chain IDs
set sel1 [atomselect top "protein and segname PROA"]
set sel2 [atomselect top "protein and segname PROB"]

# Get number of frames
set num_frames [molinfo top get numframes]

# Initialize lists to store interaction data
set hbond_data {}
set contact_data {}

# Loop through frames to analyze interactions
for {set i 0} {$i < $num_frames} {incr i} {
    animate goto $i
    # Update selections
    $sel1 frame $i
    $sel2 frame $i
    
    # Hydrogen bonds (distance < 3.5 Å, angle < 30°)
    set hbonds [measure hbonds 3.5 30 $sel1 $sel2]
    foreach {donor acceptor dist} $hbonds {
        set donor_resid [lindex [$sel1 get {resid resname}] [lindex $donor 0]]
        set acceptor_resid [lindex [$sel2 get {resid resname}] [lindex $acceptor 0]]
        lappend hbond_data "$i $donor_resid $acceptor_resid"
    }
    
    # Contacts (residues within 4 Å)
    set contacts [measure contacts 4.0 $sel1 $sel2]
    foreach {atom1 atom2} [lindex $contacts 0] {
        set res1 [lindex [$sel1 get {resid resname}] $atom1]
        set res2 [lindex [$sel2 get {resid resname}] $atom2]
        lappend contact_data "$i $res1 $res2"
    }
}

# Summarize hydrogen bond frequency
set hbond_freq {}
foreach hbond $hbond_data {
    set key [lrange $hbond 1 end]
    dict incr hbond_freq $key
}

# Summarize contact frequency
set contact_freq {}
foreach contact $contact_data {
    set key [lrange $contact 1 end]
    dict incr contact_freq $key
}

# Open a file for writing output
set outfile [open "interaction_summary.txt" "w"]

# Write frequent hydrogen bonds to file
puts $outfile "Frequent Hydrogen Bonds (>50% frames):"
dict for {key count} $hbond_freq {
    set freq [expr $count / double($num_frames)]
    if {$freq > 0.5} {
        puts $outfile "H-bond: $key, Frequency: [format \"%.2f\" $freq]"
    }
}

# Write frequent contacts to file
puts $outfile "Frequent Contacts (>50% frames):"
dict for {key count} $contact_freq {
    set freq [expr $count / double($num_frames)]
    if {$freq > 0.5} {
        puts $outfile "Contact: $key, Frequency: [format \"%.2f\" $freq]"
    }
}

# Close the output file
close $outfile

