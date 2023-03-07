#rules of these can be found on page 18 of the 26 page rule document
#note- against means roll equal to or greater than for a success

# returns whether or not the attack hits
# based upon the relevant skill(ballistics or weapon)
def doesHit(A_skill):{
    #roll a d6 against the skill
    #unmodified 6 always hits, unmodified 1 always fails
    #stretch goal-"automatically hits target" ability always hits
    #stretch goal-attack modifiers
}

# returns whether or not the attack deals damage
# baseud upon attacker strength and target toughness
def doesWound(A_strength, T_toughness):{
    #strength is compared to toughness to determine target number
    #roll d6 against said target number
    #unmodified 6 always wounds, unmodified 1 always fails
    #stretch goal-wound modifiers
}

# returns if the target unit resists damage 
# based upon Armor Penetration of weapon and Save of the target
def damageSave(A_AP, T_save):{
    #roll a d6 against the save number, modify the roll by the armor penetration
    #unmodified 6 always saves, unmodified 1 always fails
}

# updates the database of the unit to reflect the total damage recieved
# uses the saved amount of damage, the damage of the attacking weapon, 
# and the ID of the target model recieving damage <- gotta figure this one out
# since all our stuff right now is in terms of units
def inflictDamage(A_damage, T_damage_save, T_ID):{

}

#below is database access TODO: Put this in a different file

# acquires unit stats from the database using the unit id
# TODO:where it stores it is not finalized, find out if python structs are a thing
def getUnitStats(U_ID):{

}

# acquires weapon stats from the database using the weapon id
# TODO:same as getUnitStats
def getWeaponStats(W_ID):{

}
#this line here is a test to make sure everything went through correctly
#GITLAB TEST