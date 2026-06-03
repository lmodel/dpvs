---
search:
  boost: 10.0
---

# Class: CF 


_Concept representing Country of Central African Republic_



<div data-search-exclude markdown="1">



URI: [loc:CF](https://w3id.org/lmodel/dpv/loc/CF)





```mermaid
 classDiagram
    class CF
    click CF href "../CF/"
      CF <|-- CFBGF
        click CFBGF href "../CFBGF/"
      CF <|-- CFNM
        click CFNM href "../CFNM/"
      
      
```





## Inheritance
* **CF**
    * [CFBGF](CFBGF.md)
    * [CFNM](CFNM.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CF](https://w3id.org/lmodel/dpv/loc/CF) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* Central African Republic




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CF |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CF |
| native | loc:CF |
| exact | dpv_loc:CF, dpv_loc_owl:CF |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: CF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Central African Republic
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Central African Republic
exact_mappings:
- dpv_loc:CF
- dpv_loc_owl:CF
class_uri: loc:CF

```
</details>

### Induced

<details>
```yaml
name: CF
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CF
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing Country of Central African Republic
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- Central African Republic
exact_mappings:
- dpv_loc:CF
- dpv_loc_owl:CF
class_uri: loc:CF

```
</details></div>