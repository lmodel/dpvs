---
search:
  boost: 10.0
---

# Class: AT1 


_Concept representing region Burgenland in country Austria_



<div data-search-exclude markdown="1">



URI: [loc:AT-1](https://w3id.org/lmodel/dpv/loc/AT-1)





```mermaid
 classDiagram
    class AT1
    click AT1 href "../AT1/"
      AT <|-- AT1
        click AT href "../AT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [AT](AT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **AT1**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AT-1](https://w3id.org/lmodel/dpv/loc/AT-1) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* AT-1
* Burgenland




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AT-1 |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AT-1 |
| native | loc:AT1 |
| exact | dpv_loc:AT-1, dpv_loc_owl:AT-1 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AT1
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT-1
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Burgenland in country Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AT-1
- Burgenland
exact_mappings:
- dpv_loc:AT-1
- dpv_loc_owl:AT-1
is_a: AT
class_uri: loc:AT-1

```
</details>

### Induced

<details>
```yaml
name: AT1
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT-1
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Burgenland in country Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AT-1
- Burgenland
exact_mappings:
- dpv_loc:AT-1
- dpv_loc_owl:AT-1
is_a: AT
class_uri: loc:AT-1

```
</details></div>