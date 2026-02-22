# Molecule Helper

This project's code was actually created before my website, <https://bukhariayan.github.io/molymaker> as a way of first prototyping and developing the algorithms and chemistry behind the actual website. However, I adapted it so that it can also be used as an alternative. 
Simply type your compound into the terminal when prompted, and it will print information about the compound to the terminal.
while the molymaker website uses a more complex algorithm to compute bond orders, this program uses a simpler strategy that only calculates the number of bonds and lone pairs, which are necessary for the VSEPR shape. 
Because of this, it does not give information about bond order and number of sigma and pi bonds, but it does give more information about the valence electrons.

## Topics necessary for understanding the code
* interpreting chemical formulas
* electronegativity
* valence electrons
* VSEPR Theory
* bond polarity

## Libraries used
* mendeleev (for getting necessary element data such as valence electrons and electronegativities)
