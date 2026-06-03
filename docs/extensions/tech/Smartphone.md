---
search:
  boost: 10.0
---

# Class: Smartphone 


_A combination of a mobile phone with computing capabilities similar to a_

_PC_



<div data-search-exclude markdown="1">



URI: [tech:Smartphone](https://w3id.org/lmodel/dpv/tech/Smartphone)





```mermaid
 classDiagram
    class Smartphone
    click Smartphone href "../Smartphone/"
      MobilePhone <|-- Smartphone
        click MobilePhone href "../MobilePhone/"
      PersonalComputer <|-- Smartphone
        click PersonalComputer href "../PersonalComputer/"
      
      
```





## Inheritance
* **Smartphone** [ [MobilePhone](MobilePhone.md) [PersonalComputer](PersonalComputer.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Smartphone](https://w3id.org/lmodel/dpv/tech/Smartphone) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Smartphone




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#Smartphone |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Smartphone |
| native | tech:Smartphone |
| exact | dpv_tech:Smartphone, dpv_tech_owl:Smartphone |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Smartphone
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Smartphone
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A combination of a mobile phone with computing capabilities similar
  to a

  PC'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Smartphone
exact_mappings:
- dpv_tech:Smartphone
- dpv_tech_owl:Smartphone
mixins:
- MobilePhone
- PersonalComputer
class_uri: tech:Smartphone

```
</details>

### Induced

<details>
```yaml
name: Smartphone
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Smartphone
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'A combination of a mobile phone with computing capabilities similar
  to a

  PC'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Smartphone
exact_mappings:
- dpv_tech:Smartphone
- dpv_tech_owl:Smartphone
mixins:
- MobilePhone
- PersonalComputer
class_uri: tech:Smartphone

```
</details></div>