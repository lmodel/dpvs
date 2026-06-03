---
search:
  boost: 10.0
---

# Class: Criminal 


_Information about criminal activity e.g. criminal convictions or jail_

_time_



<div data-search-exclude markdown="1">



URI: [pd:Criminal](https://w3id.org/lmodel/dpv/pd/Criminal)





```mermaid
 classDiagram
    class Criminal
    click Criminal href "../Criminal/"
      Social <|-- Criminal
        click Social href "../Social/"
      

      Criminal <|-- CriminalCharge
        click CriminalCharge href "../CriminalCharge/"
      Criminal <|-- CriminalConviction
        click CriminalConviction href "../CriminalConviction/"
      Criminal <|-- CriminalOffence
        click CriminalOffence href "../CriminalOffence/"
      Criminal <|-- CriminalPardon
        click CriminalPardon href "../CriminalPardon/"
      

      
```





## Inheritance
* [Social](Social.md)
    * **Criminal**
        * [CriminalCharge](CriminalCharge.md)
        * [CriminalConviction](CriminalConviction.md)
        * [CriminalOffence](CriminalOffence.md)
        * [CriminalPardon](CriminalPardon.md)


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [pd:Criminal](https://w3id.org/lmodel/dpv/pd/Criminal) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [PdSubset](PdSubset.md)



## Aliases


* Criminal




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/pd/owl#Criminal |
| dpv_extension_slug | pd |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/pd




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | pd:Criminal |
| native | pd:Criminal |
| exact | dpv_pd:Criminal, dpv_pd_owl:Criminal |
| related | svd:Judicial |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Criminal
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Criminal
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about criminal activity e.g. criminal convictions or jail

  time'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal
exact_mappings:
- dpv_pd:Criminal
- dpv_pd_owl:Criminal
related_mappings:
- svd:Judicial
is_a: Social
class_uri: pd:Criminal

```
</details>

### Induced

<details>
```yaml
name: Criminal
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/pd/owl#Criminal
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: pd
description: 'Information about criminal activity e.g. criminal convictions or jail

  time'
in_subset:
- pd_subset
from_schema: https://w3id.org/lmodel/dpv/pd
aliases:
- Criminal
exact_mappings:
- dpv_pd:Criminal
- dpv_pd_owl:Criminal
related_mappings:
- svd:Judicial
is_a: Social
class_uri: pd:Criminal

```
</details></div>