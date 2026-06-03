---
search:
  boost: 10.0
---

# Class: ER 


_Concept representing Country of Eritrea_



<div data-search-exclude markdown="1">



URI: [loc:ER](https://w3id.org/lmodel/dpv/loc/ER)





```mermaid
 classDiagram
    class ER
    click ER href "../ER/"
      ER <|-- ERAN
        click ERAN href "../ERAN/"
      ER <|-- ERDK
        click ERDK href "../ERDK/"
      
      
```





## Inheritance
* **ER**
    * [ERAN](ERAN.md)
    * [ERDK](ERDK.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:ER](https://w3id.org/lmodel/dpv/loc/ER) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Eritrea




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#ER |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:ER |
| native | loc:ER |
| exact | dpv_loc:ER, dpv_loc_owl:ER |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ER
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ER
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Eritrea
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Eritrea
exact_mappings:
- dpv_loc:ER
- dpv_loc_owl:ER
class_uri: loc:ER

```
</details>

### Induced

<details>
```yaml
name: ER
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#ER
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Eritrea
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Eritrea
exact_mappings:
- dpv_loc:ER
- dpv_loc_owl:ER
class_uri: loc:ER

```
</details></div>