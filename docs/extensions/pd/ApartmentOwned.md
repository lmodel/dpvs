---
search:
  boost: 10.0
---

# Class: ApartmentOwned 


_Information about apartment(s) owned and its history_



<div data-search-exclude markdown="1">



URI: [pd:ApartmentOwned](https://w3id.org/lmodel/dpv/pd/ApartmentOwned)





```mermaid
 classDiagram
    class ApartmentOwned
    click ApartmentOwned href "../ApartmentOwned/"
      HouseOwned <|-- ApartmentOwned
        click HouseOwned href "../HouseOwned/"
      
      
```





## Inheritance
* [Financial](Financial.md)
    * [Ownership](Ownership.md)
        * [HouseOwned](HouseOwned.md)
            * **ApartmentOwned**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:ApartmentOwned](https://w3id.org/lmodel/dpv/pd/ApartmentOwned) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Apartment Owned




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#ApartmentOwned |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:ApartmentOwned |
| native | pd:ApartmentOwned |
| exact | dpv_pd:ApartmentOwned, dpv_pd_owl:ApartmentOwned |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ApartmentOwned
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ApartmentOwned
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about apartment(s) owned and its history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Apartment Owned
exact_mappings:
- dpv_pd:ApartmentOwned
- dpv_pd_owl:ApartmentOwned
is_a: HouseOwned
class_uri: pd:ApartmentOwned

```
</details>

### Induced

<details>
```yaml
name: ApartmentOwned
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#ApartmentOwned
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about apartment(s) owned and its history
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Apartment Owned
exact_mappings:
- dpv_pd:ApartmentOwned
- dpv_pd_owl:ApartmentOwned
is_a: HouseOwned
class_uri: pd:ApartmentOwned

```
</details></div>