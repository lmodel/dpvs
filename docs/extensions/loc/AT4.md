---
search:
  boost: 10.0
---

# Class: AT4 


_Concept representing region Upper Austria in country Austria_



<div data-search-exclude markdown="1">



URI: [loc:AT-4](https://w3id.org/lmodel/dpv/loc/AT-4)





```mermaid
 classDiagram
    class AT4
    click AT4 href "../AT4/"
      AT <|-- AT4
        click AT href "../AT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [AT](AT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **AT4**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AT-4](https://w3id.org/lmodel/dpv/loc/AT-4) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* AT-4
* Upper Austria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AT-4 |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AT-4 |
| native | loc:AT4 |
| exact | dpv_loc:AT-4, dpv_loc_owl:AT-4 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AT4
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT-4
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Upper Austria in country Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AT-4
- Upper Austria
exact_mappings:
- dpv_loc:AT-4
- dpv_loc_owl:AT-4
is_a: AT
class_uri: loc:AT-4

```
</details>

### Induced

<details>
```yaml
name: AT4
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT-4
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Upper Austria in country Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AT-4
- Upper Austria
exact_mappings:
- dpv_loc:AT-4
- dpv_loc_owl:AT-4
is_a: AT
class_uri: loc:AT-4

```
</details></div>