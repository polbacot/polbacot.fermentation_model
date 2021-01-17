# polbacot.fermentation_model

Implementation of simple toy fermentation dynamic models in Python. I made this repository for didactic puropses. 


### Batch
Operation mode: batch
State variables: substrate (glucose) and biomass
Kinetics: Monod

### Fed-batch 1
Operation mode: fed-batch
State variables: substrate(glucose), biomass, feed-rate and volume
Kinetics: Monod with substrate inhibition

* Notes: The feed-rate can be customized by the user inside the dynamics
