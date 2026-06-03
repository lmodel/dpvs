---
search:
  boost: 10.0
---

# Class: SC 


_Concept representing Country of Seychelles_



<div data-search-exclude markdown="1">



URI: [loc:SC](https://w3id.org/lmodel/dpv/loc/SC)





```mermaid
 classDiagram
    class SC
    click SC href "../SC/"
      SC <|-- SC05
        click SC05 href "../SC05/"
      SC <|-- SC08
        click SC08 href "../SC08/"
      SC <|-- SC10
        click SC10 href "../SC10/"
      SC <|-- SC14
        click SC14 href "../SC14/"
      SC <|-- SC15
        click SC15 href "../SC15/"
      SC <|-- SC24
        click SC24 href "../SC24/"
      
      
```





## Inheritance
* **SC**
    * [SC05](SC05.md)
    * [SC08](SC08.md)
    * [SC10](SC10.md)
    * [SC14](SC14.md)
    * [SC15](SC15.md)
    * [SC24](SC24.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:SC](https://w3id.org/lmodel/dpv/loc/SC) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Seychelles




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#SC |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:SC |
| native | loc:SC |
| exact | dpv_loc:SC, dpv_loc_owl:SC |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: SC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Seychelles
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Seychelles
exact_mappings:
- dpv_loc:SC
- dpv_loc_owl:SC
class_uri: loc:SC

```
</details>

### Induced

<details>
```yaml
name: SC
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#SC
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Seychelles
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Seychelles
exact_mappings:
- dpv_loc:SC
- dpv_loc_owl:SC
class_uri: loc:SC

```
</details></div>