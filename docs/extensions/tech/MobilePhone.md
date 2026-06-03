---
search:
  boost: 10.0
---

# Class: MobilePhone 


_Mobile telephone_



<div data-search-exclude markdown="1">



URI: [tech:MobilePhone](https://w3id.org/lmodel/dpv/tech/MobilePhone)





```mermaid
 classDiagram
    class MobilePhone
    click MobilePhone href "../MobilePhone/"
      Telephone <|-- MobilePhone
        click Telephone href "../Telephone/"
      

      MobilePhone <|-- Smartphone
        click Smartphone href "../Smartphone/"
      

      
```





## Inheritance
* **MobilePhone** [ [Telephone](Telephone.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:MobilePhone](https://w3id.org/lmodel/dpv/tech/MobilePhone) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Mobile Phone




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#MobilePhone |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:MobilePhone |
| native | tech:MobilePhone |
| exact | dpv_tech:MobilePhone, dpv_tech_owl:MobilePhone |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: MobilePhone
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MobilePhone
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Mobile telephone
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Mobile Phone
exact_mappings:
- dpv_tech:MobilePhone
- dpv_tech_owl:MobilePhone
mixins:
- Telephone
class_uri: tech:MobilePhone

```
</details>

### Induced

<details>
```yaml
name: MobilePhone
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#MobilePhone
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Mobile telephone
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Mobile Phone
exact_mappings:
- dpv_tech:MobilePhone
- dpv_tech_owl:MobilePhone
mixins:
- Telephone
class_uri: tech:MobilePhone

```
</details></div>