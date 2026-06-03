---
search:
  boost: 10.0
---

# Class: GM 


_Concept representing Country of Gambia_



<div data-search-exclude markdown="1">



URI: [loc:GM](https://w3id.org/lmodel/dpv/loc/GM)





```mermaid
 classDiagram
    class GM
    click GM href "../GM/"
      GM <|-- GMB
        click GMB href "../GMB/"
      
      
```





## Inheritance
* **GM**
    * [GMB](GMB.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:GM](https://w3id.org/lmodel/dpv/loc/GM) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Gambia




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#GM |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:GM |
| native | loc:GM |
| exact | dpv_loc:GM, dpv_loc_owl:GM |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: GM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Gambia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Gambia
exact_mappings:
- dpv_loc:GM
- dpv_loc_owl:GM
class_uri: loc:GM

```
</details>

### Induced

<details>
```yaml
name: GM
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#GM
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Gambia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Gambia
exact_mappings:
- dpv_loc:GM
- dpv_loc_owl:GM
class_uri: loc:GM

```
</details></div>