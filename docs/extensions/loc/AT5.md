---
search:
  boost: 10.0
---

# Class: AT5 


_Concept representing region Salzburg (state) in country Austria_



<div data-search-exclude markdown="1">



URI: [loc:AT-5](https://w3id.org/lmodel/dpv/loc/AT-5)





```mermaid
 classDiagram
    class AT5
    click AT5 href "../AT5/"
      AT <|-- AT5
        click AT href "../AT/"
      
      
```





## Inheritance
* [EEA](EEA.md)
    * [AT](AT.md) [ [EEA30](EEA30.md) [EEA31](EEA31.md) [EU](EU.md) [EU27](EU27.md) [EU28](EU28.md)]
        * **AT5**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:AT-5](https://w3id.org/lmodel/dpv/loc/AT-5) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* AT-5
* Salzburg (state)




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#AT-5 |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:AT-5 |
| native | loc:AT5 |
| exact | dpv_loc:AT-5, dpv_loc_owl:AT-5 |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: AT5
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT-5
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Salzburg (state) in country Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AT-5
- Salzburg (state)
exact_mappings:
- dpv_loc:AT-5
- dpv_loc_owl:AT-5
is_a: AT
class_uri: loc:AT-5

```
</details>

### Induced

<details>
```yaml
name: AT5
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#AT-5
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Salzburg (state) in country Austria
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- AT-5
- Salzburg (state)
exact_mappings:
- dpv_loc:AT-5
- dpv_loc_owl:AT-5
is_a: AT
class_uri: loc:AT-5

```
</details></div>