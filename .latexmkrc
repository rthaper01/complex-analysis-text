# .latexmkrc configuration for LaTeX documents with Asymptote figures
# This automates: pdflatex -> asy -> pdflatex workflow

# Use pdflatex as the main engine
$pdf_mode = 1;

# Enable shell escape for Asymptote (inline asy support)
$pdflatex = 'pdflatex -shell-escape %O %S';

# Custom dependency for .asy files
add_cus_dep('asy', 'eps', 0, 'asy2eps');
add_cus_dep('asy', 'pdf', 0, 'asy2pdf'); 

# Function to compile .asy files
sub asy2eps { return system("asy '$_[0]'"); }
sub asy2pdf { return system("asy '$_[0]'"); }

# Delete generated files when source changes to force regeneration
$clean_ext .= ' figx fls fdb_latexmk makefile';

# Clean up function that removes asymptote-generated files
sub cleanup_asy {
    unlink glob "*.figx";
    unlink glob "*.makefile"; 
    unlink glob "*-*.asy";
    unlink glob "*-*.eps";
    unlink glob "*-*.pdf";
}

# Run cleanup before each build to ensure fresh compilation
# Use a custom initialization function
$pre_tex_code = sub { cleanup_asy(); };
