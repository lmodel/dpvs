---
search:
  boost: 10.0
---

# Class: Ownership 


_Information about ownership and history, including renting, borrowing,_

_possessions_



<div data-search-exclude markdown="1">



URI: [pd:Ownership](https://w3id.org/lmodel/dpv/pd/Ownership)





```mermaid
 classDiagram
    class Ownership
    click Ownership href "../Ownership/"
      Financial <|-- Ownership
        click Financial href "../Financial/"
      

      Ownership <|-- CarOwned
        click CarOwned href "../CarOwned/"
      Ownership <|-- HouseOwned
        click HouseOwned href "../HouseOwned/"
      Ownership <|-- PersonalPossession
        click PersonalPossession href "../PersonalPossession/"
      

      
```





## Inheritance
* [Financial](Financial.md)
    * **Ownership**
        * [CarOwned](CarOwned.md)
        * [HouseOwned](HouseOwned.md)
        * [PersonalPossession](PersonalPossession.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Ownership](https://w3id.org/lmodel/dpv/pd/Ownership) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Ownership




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Ownership |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Ownership |
| native | pd:Ownership |
| exact | dpv_pd:Ownership, dpv_pd_owl:Ownership |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Ownership
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Ownership
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about ownership and history, including renting, borrowing,

  possessions'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Ownership
exact_mappings:
- dpv_pd:Ownership
- dpv_pd_owl:Ownership
is_a: Financial
class_uri: pd:Ownership

```
</details>

### Induced

<details>
```yaml
name: Ownership
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Ownership
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about ownership and history, including renting, borrowing,

  possessions'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Ownership
exact_mappings:
- dpv_pd:Ownership
- dpv_pd_owl:Ownership
is_a: Financial
class_uri: pd:Ownership

```
</details></div>