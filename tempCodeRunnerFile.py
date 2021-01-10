    ################################DOUBLE DAMAGE#########################################################
    ddm=['','']
    ddm[0]+=tp[0]
    ddm[1]+=tp[1]
    
    d_dmg_url=[]
    tp=[]
    ans1=[]
    ans2=[]
    cn=0
    for url in urls:
        poke_type=requests.get(url).json()
        for j in poke_type["damage_relations"]["double_damage_from"]:
            if not cn:
                ans1.append(j["name"])
            else:
                ans2.append(j["name"])
            tp.append(j["name"])
            d_dmg_url.append(j["url"])
            cn+=1
    Details=''
    Details="Double Damage are given by the following type: \n"
    Details+="For "+str(ddm[0])+" : "+str(ans1)+"\n"
    Details+="For "+str(ddm[1])+" : "+str(ans2)+"\n"
    window['-OUTPUT3-'].update(Details)
    
    ######################################List 5 pokemon###################################################
    Details='List 5 pokemons which gives the given pokemon double damage:\n'
    for i in range(len(d_dmg_url)):
        dat=requests.get(d_dmg_url[i]).json()
        Details+=("Pokemon of Type: "+tp[i]+'\n')
        for j in range(5):
            Details+=(dat["pokemon"][j]["pokemon"]["name"])
            if j!=4:
                Details+=(',')
        Details+=("\n\n")
    
    window['-OUTPUT4-'].update(Details)
    ##################################ABILITY###############################################################
    Details="Ability: "+str(ability(values['-INPUT-']))
    window['-OUTPUT5-'].update(Details)

window.close()