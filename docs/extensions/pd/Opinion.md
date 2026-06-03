---
search:
  boost: 10.0
---

# Class: Opinion 


_Information about opinions_



<div data-search-exclude markdown="1">



URI: [pd:Opinion](https://w3id.org/lmodel/dpv/pd/Opinion)





```mermaid
 classDiagram
    class Opinion
    click Opinion href "../Opinion/"
      Preference <|-- Opinion
        click Preference href "../Preference/"
      
      
```





## Inheritance
* [Internal](Internal.md)
    * [Preference](Preference.md)
        * **Opinion**


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Opinion](https://w3id.org/lmodel/dpv/pd/Opinion) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Opinion




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Opinion |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Opinion |
| native | pd:Opinion |
| exact | dpv_pd:Opinion, dpv_pd_owl:Opinion |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Opinion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Opinion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about opinions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Opinion
exact_mappings:
- dpv_pd:Opinion
- dpv_pd_owl:Opinion
is_a: Preference
class_uri: pd:Opinion

```
</details>

### Induced

<details>
```yaml
name: Opinion
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Opinion
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: Information about opinions
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Opinion
exact_mappings:
- dpv_pd:Opinion
- dpv_pd_owl:Opinion
is_a: Preference
class_uri: pd:Opinion

```
</details></div>