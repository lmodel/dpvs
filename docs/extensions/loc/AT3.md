---
search:
  boost: 10.0
---

# Class: AT3 


_Concept representing region Lower Austria in country Austria_



<div data-search-exclude markdown="1">



URI: [loc:AT-3](https://w3id.org/lmodel/dpv/loc/AT-3)





```mermaid
 classDiagram
    class AT3
    click AT3 href "../AT3/"
      AT <|-- AT3
        click AT href "../AT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [AT](AT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **AT3**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AT-3](https://w3id.org/lmodel/dpv/loc/AT-3) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* AT-3
* Lower Austria




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AT-3 |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AT-3 |
| native | loc:AT3 |
| exact | dpv_loc:AT-3, dpv_loc_owl:AT-3 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AT3
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT-3
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Lower Austria in country Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AT-3
- Lower Austria
exact_mappings:
- dpv_loc:AT-3
- dpv_loc_owl:AT-3
is_a: AT
class_uri: loc:AT-3

```
</details>

### Induced

<details>
```yaml
name: AT3
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT-3
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Lower Austria in country Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AT-3
- Lower Austria
exact_mappings:
- dpv_loc:AT-3
- dpv_loc_owl:AT-3
is_a: AT
class_uri: loc:AT-3

```
</details></div>