---
search:
  boost: 10.0
---

# Class: HouseOwned 


_Information about house(s) owned and ownership history_



<div data-search-exclude markdown="1">



URI: [pd:HouseOwned](https://w3id.org/lmodel/dpv/pd/HouseOwned)





```mermaid
 classDiagram
    class HouseOwned
    click HouseOwned href "../HouseOwned/"
      Ownership <|-- HouseOwned
        click Ownership href "../Ownership/"
      

      HouseOwned <|-- ApartmentOwned
        click ApartmentOwned href "../ApartmentOwned/"
      

      
```





## Inheritance
* [Financial](Financial.md)
    * [Ownership](Ownership.md)
        * **HouseOwned**
            * [ApartmentOwned](ApartmentOwned.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:HouseOwned](https://w3id.org/lmodel/dpv/pd/HouseOwned) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* House Owned




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#HouseOwned |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:HouseOwned |
| native | pd:HouseOwned |
| exact | dpv_pd:HouseOwned, dpv_pd_owl:HouseOwned |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HouseOwned
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HouseOwned
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about house(s) owned and ownership history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- House Owned
exact_mappings:
- dpv_pd:HouseOwned
- dpv_pd_owl:HouseOwned
is_a: Ownership
class_uri: pd:HouseOwned

```
</details>

### Induced

<details>
```yaml
name: HouseOwned
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#HouseOwned
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about house(s) owned and ownership history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- House Owned
exact_mappings:
- dpv_pd:HouseOwned
- dpv_pd_owl:HouseOwned
is_a: Ownership
class_uri: pd:HouseOwned

```
</details></div>