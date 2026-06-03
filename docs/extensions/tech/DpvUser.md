---
search:
  boost: 10.0
---

# Class: DpvUser 


_Actor that uses Technology_



<div data-search-exclude markdown="1">



URI: [tech:User](https://w3id.org/lmodel/dpv/tech/User)





```mermaid
 classDiagram
    class DpvUser
    click DpvUser href "../DpvUser/"
      Actor <|-- DpvUser
        click Actor href "../Actor/"
      DpvCustomer <|-- DpvUser
        click DpvCustomer href "../DpvCustomer/"
      
      
```





## Inheritance
* [Actor](Actor.md)
    * [DpvCustomer](DpvCustomer.md)
        * **DpvUser** [ [Actor](Actor.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:User](https://w3id.org/lmodel/dpv/tech/User) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* User




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/tech/owl#User |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:User |
| native | tech:DpvUser |
| exact | dpv_tech:User, dpv_tech_owl:User |
| close | iso22989:Stakeholder |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvUser
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#User
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that uses Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- User
exact_mappings:
- dpv_tech:User
- dpv_tech_owl:User
close_mappings:
- iso22989:Stakeholder
is_a: DpvCustomer
mixins:
- Actor
class_uri: tech:User

```
</details>

### Induced

<details>
```yaml
name: DpvUser
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#User
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Actor that uses Technology
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- User
exact_mappings:
- dpv_tech:User
- dpv_tech_owl:User
close_mappings:
- iso22989:Stakeholder
is_a: DpvCustomer
mixins:
- Actor
class_uri: tech:User

```
</details></div>