
#Ask the user to enter the domain of the site. for example example.com
siteDomain=input("Enter the website")

#After entering the domain, ask the user to enter a link to the 5 pages to be tested.
l1=input("Please enter 1st link:")
l2=input("Please enter 2nd link:")
l3=input("Please enter 3rd link:")
l4=input("Please enter 4th link:")
l5=input("Please enter 5th link:")

#Then display "5 pages tested on example.com".
tested_link_list=[l1,l2,l3,l4,l5]

#Add each page to a variable of type list called tested_link_list.
print("5 pages tested on  " + str(siteDomain))

#Finally, display tested pages: and print the links in the tested_link_list list.
print("print the links " + str(tested_link_list))



