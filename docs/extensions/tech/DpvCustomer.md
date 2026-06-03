---
search:
  boost: 10.0
---

# Class: DpvCustomer 


_Actor that uses Technology directly or indirectly by providing it to_

_Users_



<div data-search-exclude markdown="1">



URI: [tech:Customer](https://w3id.org/lmodel/dpv/tech/Customer)





```mermaid
 classDiagram
    class DpvCustomer
    click DpvCustomer href "../DpvCustomer/"
      Actor <|-- DpvCustomer
        click Actor href "../Actor/"
      

      DpvCustomer <|-- DpvUser
        click DpvUser href "../DpvUser/"
      

      
```





## Inheritance
* [Actor](Actor.md)
    * **DpvCustomer**
        * [DpvUser](DpvUser.md) [ [Actor](Actor.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:Customer](https://w3id.org/lmodel/dpv/tech/Customer) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Customer




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| dct_source | ISO/IEC 22989:2022 |
| upstream_iri | https://w3id.org/dpv/tech/owl#Customer |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:Customer |
| native | tech:DpvCustomer |
| exact | dpv_tech:Customer, dpv_tech_owl:Customer |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: DpvCustomer
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Customer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Actor that uses Technology directly or indirectly by providing it to

  Users'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Customer
exact_mappings:
- dpv_tech:Customer
- dpv_tech_owl:Customer
is_a: Actor
class_uri: tech:Customer

```
</details>

### Induced

<details>
```yaml
name: DpvCustomer
annotations:
  dct_source:
    tag: dct_source
    value: ISO/IEC 22989:2022
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#Customer
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Actor that uses Technology directly or indirectly by providing it to

  Users'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Customer
exact_mappings:
- dpv_tech:Customer
- dpv_tech_owl:Customer
is_a: Actor
class_uri: tech:Customer

```
</details></div>