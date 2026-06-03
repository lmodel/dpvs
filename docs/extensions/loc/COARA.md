---
search:
  boost: 10.0
---

# Class: COARA 


_Concept representing region Arauca Department in country Colombia_



<div data-search-exclude markdown="1">



URI: [loc:CO-ARA](https://w3id.org/lmodel/dpv/loc/CO-ARA)





```mermaid
 classDiagram
    class COARA
    click COARA href "../COARA/"
      CO <|-- COARA
        click CO href "../CO/"
      
      
```





## Inheritance
* [CO](CO.md)
    * **COARA**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [loc:CO-ARA](https://w3id.org/lmodel/dpv/loc/CO-ARA) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [LocSubset](LocSubset.md)



## Aliases


* CO-ARA
* Arauca Department




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/loc/owl#CO-ARA |
| dpv_extension_slug | loc |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/loc




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | loc:CO-ARA |
| native | loc:COARA |
| exact | dpv_loc:CO-ARA, dpv_loc_owl:CO-ARA |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: COARA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CO-ARA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arauca Department in country Colombia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CO-ARA
- Arauca Department
exact_mappings:
- dpv_loc:CO-ARA
- dpv_loc_owl:CO-ARA
is_a: CO
class_uri: loc:CO-ARA

```
</details>

### Induced

<details>
```yaml
name: COARA
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/loc/owl#CO-ARA
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: loc
description: Concept representing region Arauca Department in country Colombia
in_subset:
- loc_subset
from_schema: https://w3id.org/lmodel/dpv/loc
aliases:
- CO-ARA
- Arauca Department
exact_mappings:
- dpv_loc:CO-ARA
- dpv_loc_owl:CO-ARA
is_a: CO
class_uri: loc:CO-ARA

```
</details></div>