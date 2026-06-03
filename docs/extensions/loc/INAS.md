---
search:
  boost: 10.0
---

# Class: INAS 


_Concept representing region Assam in country India_



<div data-search-exclude markdown="1">



URI: [loc:IN-AS](https://w3id.org/lmodel/dpv/loc/IN-AS)





```mermaid
 classDiagram
    class INAS
    click INAS href "../INAS/"
      IN <|-- INAS
        click IN href "../IN/"
      
      
```





## Inheritance
* [IN](IN.md)
    * **INAS**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:IN-AS](https://w3id.org/lmodel/dpv/loc/IN-AS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* IN-AS
* Assam




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#IN-AS |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:IN-AS |
| native | loc:INAS |
| exact | dpv_loc:IN-AS, dpv_loc_owl:IN-AS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: INAS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IN-AS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Assam in country India
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IN-AS
- Assam
exact_mappings:
- dpv_loc:IN-AS
- dpv_loc_owl:IN-AS
is_a: IN
class_uri: loc:IN-AS

```
</details>

### Induced

<details>
```yaml
name: INAS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#IN-AS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Assam in country India
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- IN-AS
- Assam
exact_mappings:
- dpv_loc:IN-AS
- dpv_loc_owl:IN-AS
is_a: IN
class_uri: loc:IN-AS

```
</details></div>